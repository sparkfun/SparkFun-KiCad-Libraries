SparkFun Electronics KiCad Libraries
====================================

This repository contains the SparkFun KiCad Library of commonly used parts. It is a cultivated combination of KiCad parts (mostly symbols) and original SparkFun-designed Eagle footprints. This is a work in progress so be very cautious when using these symbols or footprints as they may contain errors.

**Note:** The SparkFun KiCad components contain internal part numbers for ease of manufacture for the SparkFun SMD lines. 

### Theory

KiCad is very good and has a large number of stock and industry common symbols and footprints. SparkFun has a large number of unique Eagle footprints and symbols that it has created over the years. KiCad can directly and easily import Eagle footprints, but it cannot easily import Eagle schematic symbols. Rather than converting all previous [SparkFun Eagle libraries](https://github.com/sparkfun/SparkFun-Eagle-Libraries) to KiCad, we are adding new parts to this library as we need them for new projects. This gives us the opportunity to clear out old badness, but opens the door to new badness (ie, incorrect footprints) so reader beware!

The SparkFun approach: when a new part needs to be added we decide whether to use a KiCad stock symbol, edit it for use, or create it from scratch. We give preference to the stock KiCad symbol. We give heavy preference to using the original SparkFun footprint, but look at the stock KiCad footprint for inspiration as well. We'll try to follow the [KiCad Library Conventions](https://klc.kicad.org/) where it makes sense.

Additionally, SparkFun needs to assign various unique manufacturing data (ie, internal part numbers) to parts. To alleviate this, there is a large number of components with an identical symbol each with their own production ID information. For example, capacitors:

![List of SparkFun capacitors in KiCad](Capacitor-List.png)

We use the following naming conventions to create our 'bubble gum' parts: 

* [capacity]\_[size]\_[voltage]_[tolerance]
* [resistance]\_[size]\_[wattage optional]_[tolerance optional]
* [inductance]\_[size]\_[max current]
* [led color]\_[size]\_[wavelength optional]

Contents
-------------------

* [/Footprints](https://github.com/sparkfun/SparkFun-KiCad-Libraries/tree/main/Footprints) -- PCB footprints
* [/Symbols](https://github.com/sparkfun/SparkFun-KiCad-Libraries/tree/main/Symbols) -- Schematic symbols

License
-------------------

This library is released under the [Creative Commons Attribution 4.0 International](https://creativecommons.org/licenses/by/4.0/) license. 
**You are welcome to use this library for commercial purposes.**
For attribution, we ask that when you begin to sell your device using our footprint, you email us with a link to the product being sold. 
We want bragging rights that we helped (in a very small part) to create your 8th world wonder. 
We would like the opportunity to feature your device on our homepage.

Please consider contributing back to this library or others to help the open-source hardware community continue to thrive and grow! 
