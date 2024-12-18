# Locust Selenium WebDriver Example

## Selenium Chrome Driver

You will need the Selenium chromedriver

Running:
```bash
chromedriver --version
```

Returns (something like):
```bash
ChromeDriver 123.0.6312.105 (399174dbe6eff0f59de9a6096129c0c827002b3a-refs/branch-heads/6312@{#761})
```

If `chromedriver` is not install, read this - [Learn how to install chromedriver](https://github.com/ruthlesshelp/pytest-selenium-example/blob/main/CHROMEDRIVER.md)

## Other Python Packages

For this example, you will need to install _PyQuery_

```bash
$ pip install pyquery
```

And you will need to install _Locust Plugins_

```bash
$ pip install locust-plugins
```

NOTE: The Locust Plugins 'selenium' is not installed by default, you need to install it using this command

```bash
$ pip install 'locust-plugins[webdriver]'
```


## Webdriver Example

This test is based on the Locust `examples/webdriver_ex.py`

You can find all the `locust-plugin` examples under https://github.com/SvenskaSpel/locust-plugins


# The Famous Triangle Application

This is a classic software testing exercise.

Enter the lengths of the three sides of a triangle. The program will inform you if the triangle is equilateral, isosceles or scalene.

## Triangle v001

Enter the lengths of the three sides of a triangle. The program will inform you if the triangle is equilateral, isosceles or scalene.

The website-under-test is here:
https://testpages.eviltester.com/styled/apps/triangle/triangle001.html

### Test 1

Enter into each text box
* Side 1: `599`
* Side 2: `599`
* Side 3: `599`

Click the _Identify Triangle Type_ button.

Expect the answer of "Equilateral".

### Test 2

Enter into each text box
* Side 1: `311`
* Side 2: `419`
* Side 3: `311`

Click the _Identify Triangle Type_ button.

Expect the answer of "Isosceles".

### Test 3

Enter into each text box
* Side 1: `3`
* Side 2: `4`
* Side 3: `5`

Click the _Identify Triangle Type_ button.

Expect the answer of "Scalene".

### Test 4

Enter into each text box
* Side 1: `1187`
* Side 2: `1319`
* Side 3: `79`

Click the _Identify Triangle Type_ button.

Expect the answer of "Error: Not a Triangle".
