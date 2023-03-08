user_name = input("Enter yuor name:  ")
print(user_name.lower().capitalize())

user_surname = input("Enter yuor surname:  ")
print(" , ".join(user_surname))

age = int(input("Enter yuor age:  "))
print("You were born in " + str(2023-age) + "\n")

print("Your age == 15: " + str(age == 15))
print("Your age < 15: " + str(age < 15))
print("Your age > 15: " + str(age > 15))
print("Your age == 23: " + str(age == 23))
print("Your age < 23: " + str(age < 23))
print("Your age > 23: " + str(age > 23))
print("Your age == 13: " + str(age == 13))
print("Your age < 13: " + str(age < 13))
print("Your age > 13: " + str(age > 13) + "\n")


text =  """
 Lorem ipsum dolor sit amet consectetur adipisicing elit. Corrupti, odio itaque
 mollitia hic enim ipsam a sed officiis molestias minus perferendis suscipit
 beatae amet rerum, qui fugiat adipisci, quis aperiam excepturi fugit blanditiis.
 Molestias non velit laudantium tenetur, iure sit quidem earum repellat enim
 accusantium quasi. Doloribus adipisci id, atque fugit nobis eligendi nulla
 voluptatibus earum asperiores dolores totam sint? Alias et exercitationem
 perspiciatis quisquam sunt, iure id commodi vero nesciunt harum voluptatibus,
 quia recusandae tenetur vitae ipsa iste modi corporis qui officia molestiae
 explicabo voluptas maxime necessitatibus aut? Debitis minus molestiae in labore
 id, nulla, aliquam porro fuga esse ex doloremque cumque quos repudiandae ratione
 ipsa. Modi earum, amet distinctio perspiciatis ea aperiam dignissimos quidem sed
 nulla autem quaerat soluta eum nihil iure ullam dolorem iste adipisci quasi
 asperiores? Magni dolorum atque, consequatur delectus ullam minus incidunt omnis
 culpa molestiae numquam sequi a consequuntur est, molestias accusantium
 repellendus accusamus quas dicta eveniet fugiat, natus pariatur deserunt
 excepturi. Eum, suscipit illo. Officia ipsam in aspernatur sit fuga. Laborum
 nihil enim consequatur molestias eius, labore unde! Illo consequatur officia
 doloribus quod dolore eum et ullam rerum facilis voluptatum voluptates, eaque
 veritatis est, quia quasi asperiores perferendis aliquam, ducimus aut laborum?
 Ipsam, eius culpa. Rerum, corrupti fuga?
 """
print(text.find("ad"))

print((text[0:text.find("ad")]) + (text[text.find("ad")+len("ad"):-1]))

print(text.replace("Lorem", "Hey you"))
