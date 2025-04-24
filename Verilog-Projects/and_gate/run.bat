@echo off
:: Compile
iverilog -o and_test tb_and_gate.v and_gate.v
:: Run
vvp and_test
pause
