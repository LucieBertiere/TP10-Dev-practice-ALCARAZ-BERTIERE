# TP10-Dev-practice-ALCARAZ-BERTIERE

We decided for our first ever package to do it with a well known function : fibonnaci.

But instead of just having a simple function, we also needed to take care of possible errors and having all store into a log.

So when testing oyr package onto the terminal we tested different scenarios :
- entering a non-integer value (float or string for instance)
<div align="center">

<img src="https://github.com/LucieBertiere/TP10-Dev-practice-ALCARAZ-BERTIERE/blob/main/Images/not_integer.png" width="1000" height="125">
  
</div>


- entering a negative value : at first we had no error and the program was returning a negative number, so we needed to change our code for that and put a logging error when someone tries to do so.

<div align="center">

<img src="https://github.com/LucieBertiere/TP10-Dev-practice-ALCARAZ-BERTIERE/tree/main/Images/negative_integer.png" width="450" height="275">
  
</div>

- entering a positive integer (should not raise any error)


<div align="center">

<img src="https://github.com/LucieBertiere/TP10-Dev-practice-ALCARAZ-BERTIERE/tree/main/Images/good_output.png" width="450" height="275">
  
</div>
 
