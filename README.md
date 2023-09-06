# BipBuster
this allows for precision breaks to limit computation in order to only bruteforce what bip slots you need with custom vextors of bips or the full 2048 bip list itself. This requires you to run your own cardano-node local with the cardano-wallet api, all by iohk. 
this can break into cardano wallets without the need of having all bips. It depends on conputation power but you can run throuhgh full bip lists (2048 bips) at just one bip slot.
will add the math down here so you can calc time it takes on whatever computation power you have (it is somewhere in a discord chan)

###### NOT OPTIMIZED

***wrong math will find updated version later - this was coded for crypto puzzle wallet breaking without having all bips** 

```

if we use two answers on each it takes (2^24) - 16,777,216 hits
if we limit 1 on each then brute force it takes (24*2048) - 49,152 hits


24*2048*2*3 (2 and 3 here would = 2 or 3 in a list) example of how hits grow.

!!!!!! we need to limit this for 16 so we can bruteforce !!!!!!!


right now we have
24*(3^6)*(2^6)*(4^2) - 17,915,904
17.915904 million hits - too many 


this is WITHOUT a bruteforce of *2048 ADDED (one 2^3 removed)
so we need to limit the amount of answers in each array to give computation over to 16. 
```
