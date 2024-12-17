# The Famous Triangle Application

This is a classic software testing exercise.

Enter the lengths of the three sides of a triangle. The program will inform you if the triangle is equilateral, isosceles or scalene.

For this example, you will need to install PyQuery

```bash
$ pip install pyquery
```

# Triangle v001

Enter the lengths of the three sides of a triangle. The program will inform you if the triangle is equilateral, isosceles or scalene.

The website-under-test is here:
https://testpages.eviltester.com/styled/apps/triangle/triangle001.html

## Test 1

Enter into each text box
* Side 1: `599`
* Side 2: `599`
* Side 3: `599`

Click the _Identify Triangle Type_ button.

Expect the answer of "Equilateral".

## Test 2

Enter into each text box
* Side 1: `311`
* Side 2: `419`
* Side 3: `311`

Click the _Identify Triangle Type_ button.

Expect the answer of "Isosceles".

## Test 3

Enter into each text box
* Side 1: `3`
* Side 2: `4`
* Side 3: `5`

Click the _Identify Triangle Type_ button.

Expect the answer of "Scalene".

## Test 4

Enter into each text box
* Side 1: `1187`
* Side 2: `1319`
* Side 3: `79`

Click the _Identify Triangle Type_ button.

Expect the answer of "Error: Not a Triangle".
