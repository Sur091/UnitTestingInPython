```lean
def fibonacci (n : Nat) : Nat :=
  if n < 2 then n
  else fibonacci (n - 1) + fibonacci (n - 2)

#eval fib_no_pm 10  -- Expected output: 55
```
