# Vending Machine app

## Run app

```
python main.py
```

## Available commands

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
