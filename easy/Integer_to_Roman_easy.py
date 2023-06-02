def intToRoman(num: int) -> str:
        roman=''
        while num==0:
            if num>=1000:
                for i in range(0,num/1000):
                    roman=roman+'M'
                num=num/1000
            elif num>=900:
                for i in range(0,num/900):
                    roman=roman+'CM'
                num=num/900
            elif num>=500:
                for i in range(0,num/500):
                    roman=roman+'D'
                num=num/500
            elif num>=400:
                for i in range(0,num/400):
                    roman=roman+'CD'
                num=num/400
            elif num>=100:
                for i in range(0,num/100):
                    roman=roman+'C'
                num=num/100
            elif num>=90:
                for i in range(0,num/90):
                    roman=roman+'XC'
                num=num/90
            elif num>=50:
                for i in range(0,num/50):
                    roman=roman+'L'
                num=num/50
            elif num>=40:
                for i in range(0,num/40):
                    roman=roman+'XL'
                num=num/40
            elif num>=10:
                for i in range(0,num/10):
                    roman=roman+'X'
                num=num/10
            elif num>=9:
                for i in range(0,num/9):
                    roman=roman+'IX'
                num=num/9
            elif num>=5:
                for i in range(0,num/5):
                    roman=roman+'V'
                num=num/5
            elif num>=4:
                for i in range(0,num/4):
                    roman=roman+'IV'
                num=num/4
            elif num>=1:
                for i in range(0,num/1):
                    roman=roman+'I'
                num=0
            return roman
