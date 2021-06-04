def help
  help="""\t\t ==> welecome to shoping list app <== !!
you can enter all thing to save on your shop list.
sure!, use the show to show item of your list
and you can use the count to show the  count of item on your list
and use the clear to cleared display app
for exit of app , use exit\n
\t\t ***THANKS YOU FOR SEE MY !!*** \n
"""
 puts help
end
def main
  system("clear")
  text="""\t\t ==> welcome to Shoping List <==\n
Hi, my name is 'atom',i'am first robot on app !
this is app for lists the all things for Shoping
for see the more of help you can use the help\n
"""
  shop=[]
  delete=[]
  puts text
  while true
      print"SAJAD ~$ "
      command=gets.chomp
      if command == "exit"
        break
      elsif command == "clear"
        system("clear")
      elsif command == "show"
        for i in shop
          puts "[+] #{i}"
        end
      elsif command == "help"
        help
      elsif command == "count"
         count=0
         for i in shop
           count+=1
         end
         puts"the count of item on shop lists ==> #{count}"

      else
         shop.append(command)
      end
  end
end
main
