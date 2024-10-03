def main():
    print(fuel_calculation())


def fuel_calculation():

    while True:
        try:
            fuel_level = input("Please enter a fraction of fuel left.  ")
            num, denom = (fuel_level.split('/'))
            fuel_level = round((float(num)/float(denom))*100)
            
            if fuel_level < 0:
                print("Fraction cannot be less than 0")
                continue
            
            elif fuel_level > 100:
                print("Fraction cannot be greater than 1")
                continue
        
            elif fuel_level >= 99:
                return f"Fuel Level is F"
    
            elif fuel_level <= 1:
                return f"Fuel Level is E"
            
                       
        except ValueError:
            print("Fraction needs to be a numerical fraction!")

        except ZeroDivisionError:
            print("Fraction cannot be divisible by zero!")

        else:
            return f"Fuel Level is {fuel_level}%"

main()

