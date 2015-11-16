# py-console
Style output and write to a specific position in the terminal.

## Usage


```
import console

console.write('Hello')
console.write(',Python!')

> Hello, Python!

console.writeLine('Hello')
console.writeLine('Python!')

> Hello
> Python!
```

## Style output

The first argument is the text output and all following arguments are for styling.
```
console.writeLine(text, *style)
```
### Usage
```
console.writeLine('Hello, Pyhton!')

console.writeLine('This text line will be green', console.green)

console.writeLine('Reverse the green color', console.green, console.reverse)
```

##### Style attributes

| Code               | Description                          |
| :----------------- | :----------------------------------- |
| console.off        | All attributes off                   |
| console.bold       | Bold                                 |
| console.dim        | Dim                                  |
| console.underscore | Underscore (monochrome display only) |
| console.blink      | Blink                                |
| console.reverse    | Reverse                              |
| console.hide       | Hide                                 |

##### Text color

| Code            | Color       |
| :-------------- | :---------- |
| console.black   | Black       |
| console.red     | Red         |
| console.Green   | Green       |
| console.yellow  | Yellow      |
| console.blue    | Blue        |
| console.Magenta | Magenta     |
| console.cyan    | Cyan        |
| console.white   | White       |

##### Background color

| Code              | Color       |
| :---------------- | :---------- |
| console.bgblack   | Black       |
| console.bgred     | Red         |
| console.bggreen   | Green       |
| console.bgyellow  | Yellow      |
| console.bgblue    | Blue        |
| console.bgMagenta | Magenta     |
| console.bgcyan    | Cyan        |
| console.bgwhite   | White       |


## Cursor position

Move the cursor to a specific position.
```
console.position(line, column)

console.position(2, 15)
```

Move the cursor to a home position (1, 1).
```
console.homePos()
```

Moves the current cursor position up, down, left or right by the specified value.
```
console.up(value)
console.down(value)
console.left(value)
console.right(value)
```

Saves the current cursor position.
```
console.saveCursor()
```

Restore the previously stored cursor position.
```
console.restoreCursor()
```

Clear the terminal screen.
```
console.clear()
```

Clear the entire line of on the current cursor position.
```
console.clearLine()
```

Clear line from the current cursor position to the end.
```
console.clearLineFromPos()
```

Clear line from begin to current cursor position.
```
console.clearLineToPos()
```

## Licence

The MIT License (MIT)

Copyright (c) 2015 René Tanczos

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
