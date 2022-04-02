@echo off
if %1==-f (
  setlocal EnableDelayedExpansion
  set opts=
  for /f "tokens=* delims=" %%x in (%2) do set opts=!opts!%%x
  python bfr.py !opts!
)
if %1==-e (
  python bfr.py %~2
)
