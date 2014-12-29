REM set "var=%cd%"
REM cd var

pushd %~dp0

@echo off
set PATH=%PATH%;C:\Program Files\Git\bin

ipython notebook

