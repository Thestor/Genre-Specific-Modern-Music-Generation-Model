from constants import *
import generate

def main():
    number = 1
    
    print("WELCOME TO MUSIC GENERATION APPLICATION")
    print("Please select one or more styles to begin (separated by space).\n\n")
    
    print("0.", "all genres - no specified style\n")
    
    for i in styles:
        for j in i:
            split_entry = j.split("/")
            print(str(number)+".", split_entry[2], "(" + j.split("/")[1] + ")")
            number += 1
            
    while True:
        selected_style = input("\nEnter your desired style = ").strip()
        split_style = selected_style.split()
        how_many = len(split_style)
        final_styles = ""
        
        if how_many <= 0:
            print("Input at least one style!\n")
            
        elif how_many == 1:
            selected_style = split_style[0]
            if selected_style.isnumeric():
                selected_style = int(selected_style)
                if selected_style == 0:
                    final_styles = None
                    break;
                elif selected_style > number - 1:
                    print("Style", selected_style, "doesn't exist!")
                else:
                    final_styles = str(selected_style - 1)
                    break;
            else:
                print("Input a valid number!")
            
        else:
            valid_multiple_styles = True
            for each_style in split_style:
                if each_style.isnumeric():
                    each_style = int(each_style)
                    if each_style == 0:
                        print("Multiple style selections do not allow 0.\n")
                        valid_multiple_styles = False
                    elif each_style > number - 1:
                        print("Style", each_style, "doesn't exist!")
                        valid_multiple_styles = False
                    else:
                        final_styles = final_styles + str(each_style - 1) + " "
                else:
                    print("Input a valid number!")
            
            if (valid_multiple_styles):
                final_styles.rstrip();
                break
            
    while True:
        no_of_bars = input("\nEnter the number of bars = ")
        if no_of_bars.isnumeric():
            no_of_bars = int(no_of_bars)
            if no_of_bars < 4:
                print("Four bars minimum.\n")
            else:
                break
        else:
            print("Input a valid number!/n")   

    print("--bars", str(no_of_bars), "--styles", str(final_styles))
    generate.generate_music(final_styles, no_of_bars)
    
if __name__ == '__main__':
    main()
                

            
    
      