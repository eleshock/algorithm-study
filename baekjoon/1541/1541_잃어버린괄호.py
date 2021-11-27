"""백준 1541번 잃어버린 괄호 https://www.acmicpc.net/problem/1541"""
"""문제
세준이는 양수와 +, - 그리고 괄호를 가지고 식을 만들었다.
그리고 나서 세준이는 괄호를 모두 지웠다.
세준이는 괄호를 적절히 쳐서 이 식의 값을 최소로 만들려고 한다.
괄호를 적절히 쳐서 이 식의 값을 최소로 만드는 프로그램을 작성하시오

식은 0 ~ 9, +, - 만으로 이뤄져 있다. 
가장 처음과 마지막 문자는 숫자이다.
그리고 연속해서 두 개 이상의 연산자가 나타나지 않고, 5자리보다 많이 연속되는 숫자는 없다.
수는 0으로 시작할 수 있다. 입력으로 주어지는 식의 길이는 50보다 작거나 같다.

예제 입력
    55-50+40
"""

import sys

equation = sys.stdin.readline().strip().split('-')

result = 0

for i in equation[0].split('+'):
    result += int(i)

for i in equation[1:]:
    for j in i.split('+'):
        result -= int(j)

print(result)