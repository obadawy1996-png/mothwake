#!/usr/bin/env bash
# Negative tests: each injected violation must make the verifier FAIL.
# All fixtures are created in a throwaway temp dir or removed immediately after.
set -u
cd "$(dirname "$0")/.."
PY=.venv/bin/python
V=scripts/verify_isolation.py
T=$(mktemp -d)
pass=0; fail=0
expect() { # name, expected_exit, cmd...
  local name=$1 want=$2; shift 2
  "$@" >"$T/out" 2>&1; local got=$?
  if [ "$got" = "$want" ]; then echo "[PASS] $name"; pass=$((pass+1));
  else echo "[FAIL] $name (exit $got, wanted $want)"; sed 's/^/    /' "$T/out"; fail=$((fail+1)); fi
}

expect "clean project verifies"                 0 $PY $V verify

# 1. tampered baseline is detected
$PY - "$T/bad.json" <<'EOF'
import json,sys
b=json.load(open(".isolation/baseline.json"))
k=next(iter(b["targets"])); f=next(iter(b["targets"][k])); b["targets"][k][f]="0"*64
json.dump(b,open(sys.argv[1],"w"))
EOF
expect "altered protected fingerprint fails"    1 env MOTHWAKE_BASELINE="$T/bad.json" $PY $V verify

# 2. a simulated Chrono Tales folder that appears after baseline is flagged
mkdir -p "$T/root/Chrono-Tales-Cinema"
expect "new unbaselined Chrono location fails"  1 env MOTHWAKE_SEARCH_ROOTS="$T/root" $PY $V verify

# 3. symlink escaping the project fails
ln -s /etc docs/_escape_test
expect "escaping symlink fails"                 1 $PY $V verify
rm docs/_escape_test

# 4. a project file referencing Chrono Tales fails
echo "copy assets from chrono-tales" > config/_ref_test.txt
expect "Chrono reference in project fails"      1 $PY $V verify
rm config/_ref_test.txt

# 5. running outside the project venv fails
expect "system python (not venv) fails"         1 /usr/bin/python3 $V verify

expect "clean again after cleanup"              0 $PY $V verify
rm -rf "$T"
echo; echo "$pass passed, $fail failed"
[ "$fail" = 0 ]
