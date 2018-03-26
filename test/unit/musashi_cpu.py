import pytest
from musashi import emu
from musashi.m68k import *


def musashi_cpu_rw_reg_test():
  cpu = emu.CPU(M68K_CPU_TYPE_68000)
  cpu.w_reg(M68K_REG_D0, 0xdeadbeef)
  assert cpu.r_reg(M68K_REG_D0) == 0xdeadbeef
  # invalid values
  with pytest.raises(OverflowError):
    cpu.w_reg(M68K_REG_D0, 0xdeadbeef12)
  with pytest.raises(OverflowError):
    cpu.w_reg(M68K_REG_D0, -1)
  with pytest.raises(TypeError):
    cpu.w_reg(M68K_REG_D0, "hello")


def musashi_cpu_rws_reg_test():
  cpu = emu.CPU(M68K_CPU_TYPE_68000)
  cpu.ws_reg(M68K_REG_D0, -123)
  assert cpu.rs_reg(M68K_REG_D0) == -123
  # invalid values
  with pytest.raises(OverflowError):
    cpu.ws_reg(M68K_REG_D0, 0x80000000)
  with pytest.raises(OverflowError):
    cpu.ws_reg(M68K_REG_D0, -0x80000001)
  with pytest.raises(TypeError):
    cpu.ws_reg(M68K_REG_D0, "hello")
