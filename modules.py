from func import double_it
from kargs_multiple import famous_name as f_name # as দিয়ে ফাইলের সংক্ষেপ নাম কে বুঝায়
from default_params import * # একটা ফাইলের সকল নাম ইমপোর্ট করতে এই * সাইন ব্যবহার করা হয়।
# output = double_it(112)
# print(output)
name_output = f_name(first="alu", last="kodu", title="joss", addition="komu na")
print(name_output)