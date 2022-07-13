# Vending Machine app

## Install python >= 3.8x

https://www.python.org/downloads/

We are not going to use virtual environment since we do not use any external packages.

## Clone the project from GitHub

```
git clone https://github.com/pfbox/vendingmachine.git
```

## Run app

```
cd vendingmaching
python3 main.py
```

## Available commands
This app is using prompt input to operate 
```
healthcheck - show vending machine info
menu - show menu
item {i}, i=Candy/Soda/Chips  
pay {c}, c=5/10/25/100/200/500/1000/2000, 5c-$20 
refund
exit
```

## Examples
```
>menu
(Name: Candy, Price: 200)
(Name: Chips, Price: 150)
(Name: Soda, Price: 100)
```
```
>pay 25
The amount of 25 has been paid
Total credit is 25
```
```
>item Chips
Item Chips served
Current credit is 75
```
```
>refund
Refunded {200: 1, 25: 1, 5: 1}, total refund 230
```

## Improvements
 - Use codes instead of names
 - Add/delete item from the menu
 - Logging/tracking
 - One word command 
 - Admin access
 - Add sophisticated checking (e.g. if you put a bill but no merchandise nor change available)
 - Add unit/integration tests
