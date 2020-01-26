# most of test cases copied from https://github.com/kanaka/mal/tree/master/tests

import pytest
import sys
import os
sys.path.append(os.path.abspath('test'))
from runner import execute, Interpreter

def test_strings_equalitf():
    run = Interpreter().run
    assert run('(= "" "")') == "true"
    assert run('(= "abc" "abc")') == "true"
    assert run('(= "abc" "")') == "false"
    assert run('(= "" "abc")') == "false"
    assert run('(= "abc" "def")') == "false"
    assert run('(= "abc" "ABC")') == "false"
    assert run('(= (list) "")') == "false"
    assert run('(= "" (list))') == "false"

    assert run('(if "" 7 8)') == '7'

    assert run('(not false)') == 'true'
    assert run('(not nil)') == 'true'
    assert run('(not true)') == 'false'
    assert run('(not "a")') == 'false'
    assert run('(not 0)') == 'false'

    assert run('""') == '""'
    assert run('"abc"') == '"abc"'
    assert run('"abc  def"') == '"abc  def"'
    assert run('"\\""') == '"\\""'
    assert run('"abc\\ndef\\nghi"') == '"abc\\ndef\\nghi"'
    assert run('"abc\\\\def\\\\ghi"') == '"abc\\\\def\\\\ghi"'
    assert run('"\\\\n"') == '"\\\\n"'
