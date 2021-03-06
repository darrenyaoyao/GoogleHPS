# GSensor
![MCP3008_wiring](https://user-images.githubusercontent.com/31827037/128541790-2995bc43-6a1d-411e-b15c-5929e3833f3a.jpg)

Open SPI interface in Raspberry Pi Setting first

## Wiring
### Raspberry pi GPIOs
![Raspberry Pi GPIO](https://user-images.githubusercontent.com/31827037/129449383-edb58c4d-ee2c-483e-a50f-96c32c704b8c.png)
### MCP3008 Pins
![mcp3008](https://user-images.githubusercontent.com/31827037/129449405-79bd1746-ca7b-4858-a82d-31bbf400697a.gif)

### Digital Side
* MCP3008 VDD -> 3.3V (red)
* MCP3008 VREF -> 3.3V (red)
* MCP3008 AGND -> GND (black)
* MCP3008 CLK -> SCLK (yellow)
* MCP3008 DOUT -> MISO (purple)
* MCP3008 DIN -> MOSI (white)
* MCP3008 CS -> GPIO8 (green)
* MCP3008 DGND -> GND (black)
### Analog Side
* Pin #1 (left) goes to 3.3v (red)
* Pin #2 (middle) connects to MCP3008 CH0 (analog input #0) with a purple wire
* Pin #3 (right) connects to GND (black)

### More detail
you can follow [link](https://learn.adafruit.com/raspberry-pi-analog-digital-converters/mcp3008)

