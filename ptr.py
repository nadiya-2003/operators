
'''
You are given principal amount, rate of interest per annum, and time in years. You need to calculate the simple interest.
Input and Output Format
Input Format:
The first line contains the principal amount (principal).
The second line contains the rate of interest (rate) per annum.
The third line contains the time (time) in years.
Output Format:
A single line containing the simple interest calculated.
Sample Input 1
1000
5
2
Sample Output 1
100.0
Sample Input 2
5000
8.5
3
Sample Output 2
1275.0
Sample Input 3
5000
8.5
3
Sample Output 3
525.0
'''
def calculate_simple_interest():
    
    principal = float(input("Enter the principal amount: "))
    rate = float(input("Enter the rate of interest per annum: "))
    time = float(input("Enter the time in years: "))
    
 
    simple_interest = (principal * rate * time) / 100
    
   
    print(f"{simple_interest:.1f}")

if __name__ == "__main__":
    calculate_simple_interest()

