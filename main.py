## this is my main file

## import modules
import adder, greeter, dbs

## call with module.function()

## call the first function in adder module
value = adder.add(2,2)
print(value)
dvalue = adder.double(value)
print(dvalue)

print(greeter.greet("Mike"))