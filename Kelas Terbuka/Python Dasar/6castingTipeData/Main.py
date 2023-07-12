#Belajar casting
#Casting adalah merubah ke tipe data yang lain
#Macam tipe data : integer, float, boolean, and string

##INTEGER
print("====INTEGER====")
data_int = 15;
print("value",data_int, "tipe data",type(data_int))

data_float = float(data_int)
data_str   = str(data_int)
data_bool  = bool(data_int)
print("value",data_float, "tipe data",type(data_float))
print("value",data_str, "tipe data",type(data_str))
print("value",data_bool, "tipe data",type(data_bool))

##FLOAT
print("====FLOAT====")
data_float = 15.42;
print("value",data_float, "tipe data",type(data_float))

data_int = int(data_float)
data_str   = str(data_float)
data_bool  = bool(data_float)
print("value",data_int, "tipe data",type(data_int))
print("value",data_str, "tipe data",type(data_str))
print("value",data_bool, "tipe data",type(data_bool))

##BOOLEAN
#Jika nilai bool True = 1 jika False = 0
print("====BOOLEAN====")
data_bool = True;
print("value",data_bool, "tipe data",type(data_bool))

data_float = float(data_bool)
data_str   = str(data_bool)
data_int   = int(data_bool)
print("value",data_float, "tipe data",type(data_float))
print("value",data_str, "tipe data",type(data_str))
print("value",data_int, "tipe data",type(data_int))

##STRING
print("====STRING====")
data_str = "15";
print("value",data_str, "tipe data",type(data_str))

data_float = float(data_str) #Jika nilai string angka bisa di casting selain itu not is can
data_int   = int(data_str) #Jika nilai string angka bisa di casting selain itu not is can
data_bool  = bool(data_str) #Jika ada huruf / angka = True jika tidak ada = False
print("value",data_float, "tipe data",type(data_float))
print("value",data_int, "tipe data",type(data_int))
print("value",data_bool, "tipe data",type(data_bool))