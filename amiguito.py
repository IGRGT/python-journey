# Amiguito (in progress)
# Created by Gilberto Ruiz
# Date: 06-10-2026





# TODO: time based decay once we move to tkinter

import time

import random

import json


#information for the learn command :
short_facts = ["Python is named after Monty Python's Flying Circus, not the snake. Guido van Rossum was reading Monty Python scripts while writing it in 1989.",
    "There are only 13 root DNS server *addresses* (A through M), but hundreds of physical machines worldwide serve them using anycast routing — traffic hits the closest one.",
    "MD5 was cryptographically broken in 2004. Today you can compute a collision in seconds. SHA-1 was broken in 2017 by Google's SHAttered attack.",
    "GPS would be wrong by ~10 km per day without Einstein. Satellite clocks gain 45 microseconds/day from weaker gravity and lose 7 from orbital speed. The net difference is corrected in real time.",
    "CPython caches integers from -5 to 256. So `a = 256; a is b` is True, but `a = 257; a is b` is False. 'is' checks identity, not value — always use '=='.",
    "Python integers never overflow. `2**1000` returns a 302-digit number. In C, a 64-bit int overflows at 9,223,372,036,854,775,807.",
    "Type `import this` in any Python shell to read the Zen of Python — 19 guiding principles embedded in every Python install.",
    "The Halting Problem (Turing, 1936) proves no algorithm can determine whether an arbitrary program halts or runs forever. Perfect malware detection is mathematically impossible.",
    "BGP — the protocol routing traffic between internet providers — has no authentication by default. In 2010, China Telecom accidentally hijacked routes for the US military, Dell, and CNN for ~18 minutes.",
    "Cosmic rays can flip bits in RAM. High-energy particles ionize silicon and flip a stored bit. ECC RAM exists specifically to detect and correct this. The effect is 100x worse at high altitude.",
    "HTTPS hides your content, not who you're talking to. Your DNS queries are often unencrypted, so your ISP can see exactly which domains you visit even when all content is encrypted.",
    "A /24 subnet has 256 addresses but only 254 usable ones — .0 is the network address, .255 is broadcast. A /30 gives just 2 usable hosts and is used for point-to-point links.",
    "An HDD read head never touches the disk. It floats 3-5 nanometers above the spinning surface on a cushion of air — thinner than a smoke particle and 20x thinner than a red blood cell.",
    "AES was not invented by NIST. It won a public competition in 2001. The algorithm is called Rijndael, created by two Belgian cryptographers. NIST evaluated 14 submissions over 5 years.",
    "Accessing RAM from a modern CPU takes ~200-300 clock cycles. An L1 cache hit takes 1-4. CPUs are often completely idle just waiting for data to arrive.",
    "NVMe SSDs (PCIe) can hit 7,000 MB/s reads. SATA SSDs max at 600 MB/s no matter how fast the drive hardware is — the SATA interface itself is the bottleneck, built for spinning disks.",
    "DNS uses port 53 UDP for queries but switches to port 53 TCP for responses over 512 bytes. The 512-byte UDP limit is why DNSSEC responses sometimes break on old resolvers.",
    "The OSI model was published in 1984 but the real internet runs on TCP/IP, which predates it. OSI is a teaching framework, not an implementation spec.",
    "Password salting defeats rainbow tables. A rainbow table is a precomputed hash→password lookup. Adding a unique random salt to each password means an attacker needs a separate table per user — infeasible.",
    "TCP's congestion control was designed by Van Jacobson in 1988 after a collapse reduced ARPANET throughput by 1000x. His patch roughly doubled internet throughput when deployed.",]


long_facts = ["DRAM stores each bit as a charge on a capacitor that leaks, so it must be electrically refreshed thousands of times per second. SRAM (used in CPU caches) doesn't leak, but uses 6 transistors per bit versus 1 for DRAM — making SRAM roughly 30x larger and more expensive per bit. This tradeoff is why your CPU has small, fast cache and large, slow main memory. The gap between them is called the von Neumann bottleneck, and it's one of the core performance problems in modern computing.",

    "Virtual memory gives every process its own isolated address space. A 64-bit process thinks it owns all of memory, but the OS maps 4KB chunks called 'pages' to physical RAM on demand. When a page isn't in RAM, a page fault triggers and the OS loads it from disk — the program never knows this happened. This is how your computer runs more programs than would physically fit in RAM, and how one process can't read another process's memory.",

    "When a Unix process calls fork(), the child doesn't immediately copy the parent's memory. Pages are shared read-only until either process writes to one, at which point the kernel copies only that specific page. This is called copy-on-write. It makes forking nearly instant regardless of how much memory the parent is using — the OS is lazy about doing the actual work.",

    "HTTPS uses asymmetric encryption (RSA or ECDH) only during the handshake to establish a shared key. All actual data transfer uses symmetric AES, because symmetric ciphers are roughly 1000x faster. The asymmetric step solves the key exchange problem — how two strangers agree on a secret over a public channel — not the encryption problem itself. This hybrid approach is the foundation of basically all secure communication on the internet.",

    "Backpropagation is just the chain rule of calculus applied repeatedly through a computation graph. Rumelhart, Hinton, and Williams popularized it in a 1986 Nature paper, but the algorithm was discovered independently multiple times since the 1960s — nobody had hardware fast enough to make it useful. During training, the network makes a prediction, computes how wrong it was (the loss), then propagates that error backward through each layer, adjusting weights proportionally to how much each one contributed to the mistake.",

    "The vanishing gradient problem: in deep networks, gradients are multiplied through each layer during backpropagation. With sigmoid activations, gradients shrink by up to 4x per layer — after 10 layers they're effectively zero and nothing learns. ReLU activations (gradient of exactly 1 for positive inputs) and residual connections (skip connections in ResNet, 2015) largely solved this and enabled modern networks with hundreds of layers.",

    "AlexNet won the 2012 ImageNet competition with a top-5 error of 15.3% versus 26.2% for second place. The gap was so large it shocked the field and triggered the modern deep learning era. It ran on two consumer GTX 580 GPUs with 3GB RAM each. The key ingredient wasn't the architecture — it was training on GPUs, which made the whole thing feasible in weeks instead of years.",

    "Transformers (introduced in 'Attention Is All You Need,' 2017) replaced recurrence with self-attention: every token directly attends to every other token in the sequence. This removed the sequential bottleneck of RNNs, made training massively parallelizable on GPUs, and enabled scaling to billions of parameters. Every major language model today (GPT, Claude, Gemini) is built on this architecture.",

    "Spectre and Meltdown (disclosed January 2018) exploited speculative execution — a technique where CPUs run instructions before they know if they're needed, to save time. The flaw: a program could trick the CPU into speculatively reading memory it shouldn't have access to, then measure the timing of cache accesses to reconstruct the secret data. The OS-level patches that fixed this slowed some workloads by 5-30% because safe speculation is fundamentally slower.",

    "The birthday paradox sets a concrete collision bound for hash functions. To have a 50% chance of a collision in any hash with N possible outputs, you only need roughly the square root of N inputs. For SHA-256 with 2^256 outputs, that's 2^128 attempts — still infeasible, but it explains why 256-bit hashes don't give you 256-bit security against all attacks. The paradox is named because in a room of just 23 people, there's already a 50% chance two share a birthday — far fewer than you'd intuitively expect.",

    "Thrashing happens when the total working set of all running processes exceeds available RAM. The OS spends more CPU time swapping pages in and out of disk than actually executing instructions — the machine slows to a crawl. Adding more processes makes it catastrophically worse. The correct fix is more RAM or reducing the number of active processes, not adjusting swap settings. This is why servers carefully limit concurrent process counts.",

    "The Universal Approximation Theorem (Cybenko, 1989) proves that a single hidden layer of neurons with enough units can approximate any continuous function to arbitrary precision. It sounds like a guarantee that neural nets can learn anything — but it doesn't say how many neurons you need, how to train them, or whether your optimizer will find the solution. It's an existence proof, not a recipe. Deep networks turned out to work better in practice for reasons that are still being fully understood.",]


items = {
        "apple" :{"stat": "fullness", "amount": 10, "message": "You have an apple! Eating it will increase your fullness."},
        "ball": {"stat": "happiness", "amount": 10, "message": "You have a ball! Playing with it will increase your happiness."},
        "blanket": {"stat": "energy", "amount": 10, "message": "You have a blanket! Hugging it will increase your energy."},
        }

def display_menu():
    print("Here are some things you can do with Amiguito:")
    print("- feed: to give Amiguito some food and increase fullness")
    print("- play: to play games and increase happiness")
    print("- chat: to have a conversation and increase happiness")
    print("- learn: to learn new things and increase happiness")
    print("- rest: to take a break and increase energy")
    print("- drink: to have some water and increase thirst")
    print("- stats: to see Amiguito's current stats")
    print("- mood: to see how Amiguito is feeling based on their stats")
    print("- exit: to end the conversation")

def check_mood(stats):return (stats)["fullness"] > 30 and stats["thirst"] > 30 and stats["energy"] > 30 and stats["happiness"] > 30
    
def clamp_stats(stats):
    for key in ["fullness", "thirst", "energy", "happiness"]:
            if stats[key] > 100:
                stats[key] = 100
            if stats[key] < 0:
                stats[key] = 0

class Pet:
    def __init__(self, name):
        self.name = name

        self.inventory = ["apple", "ball", "blanket"]
        try:
            with open("amiguito_state.json", "r") as file:
                data = json.load(file)
                self.stats = data["stats"]
                self.inventory = data["inventory"]

                
        except FileNotFoundError:
                self.stats = {"last_updated": time.time(), "fullness": 80, "thirst": 80, "energy": 80, "happiness": 80}
                self.inventory = ["apple", "ball", "blanket"]
    def show_stats(self):
        print ()
        print()
        print("---Fullness:", self.stats["fullness"], "/100---")
        print()
        print("---Thirst:", self.stats["thirst"], "/100---")
        print()
        print("---Energy:", self.stats["energy"], "/100---")
        print()
        print("---Happiness:", self.stats["happiness"], "/100---")
        print()
        print ()
      

    def state_of_being(self):
        if self.stats["fullness"] < 30:
            print ()
            print ("I am feeling hungry. Maybe we should get some food soon!")
        if self.stats["thirst"] < 30:
            print ()
            print("I am feeling thirsty. Let's make sure to have some water nearby!")
        if self.stats["energy"] < 30:
            print()
            print("I am feeling tired. A little rest might do the trick!")
        if self.stats["happiness"] < 30:
            print ()
            print("I am feeling bored. Let's find something fun to do together!")
    
    def add_to_inventory(self, item):
        self.inventory.append(item)
        print(f"{item} has been added to my inventory.")

    def use_item(self, item):
        if item == "apple":
            print("You have an apple! Eating it will increase your fullness.")
            self.stats["fullness"] += 10
            clamp_stats(self.stats)
            self.show_stats()
        if item == "ball":
            print("You have a ball! Playing with it will increase your happiness.")
            self.stats["happiness"] += 10
            clamp_stats(self.stats)
            self.show_stats()
        if item == "blanket":
            print("You have a blanket! Using it will increase your energy.")
            self.stats["energy"] += 10
            clamp_stats(self.stats)
            self.show_stats()

amiguito = Pet("amiguito")
stats = amiguito.stats




space = "--" * 60

history = []


likes_to = "play games, learn new things, and chat with people!"












print()  
print()
print(space)
print()
print("Hello! I am Amiguito 2.5 I am a work in progress, I am here to interact, play games, and learn new things with you. Let's have some fun together!")  
display_menu()
print()



amiguito.show_stats()

while True:
    now = time.time()
    elapsed = now - stats["last_updated"]
    
    for key in ["fullness", "thirst", "energy", "happiness"]:
        stats[key] -= elapsed * (1/60)
        stats[key] = round(stats[key],1)
    stats["last_updated"] = now
    

    all_good = check_mood(stats)
    not_so_good = not check_mood(stats)
    print()
    topic = input("What would you like to do? ")
    history.append(topic)
    
    if topic.lower() == "feed":
        print("Yum! Amiguito loves food! Let's find something delicious to eat together!") 
        stats["fullness"] += 10
    elif topic.lower() == "what do you like to do?":
        print()
        print(likes_to)
        print()


    elif topic.lower() == "play":
        print()
        print("Lets play guess the number!")
        secret_number = random.randint(1, 100)
        guesses = 0

        while True:
            guess = int(input("Guess a number from 1 to 100: "))  
            guesses += 1

            if guess < secret_number:
                print("Too low!")
            elif guess > secret_number:
                print("Too high!")
            
            if guess == secret_number:
                print (f"You got it in {guesses} guesses!")
                break  
            if guesses >= 10:
                print("You're out of tries, the right answer was: ", secret_number)
                break
        

        stats["happiness"] += 10



    elif topic.lower() == "chat":
        print("Great! Amiguito loves to chat! What would you like to talk about?")
        stats["happiness"] += 5
    elif topic.lower() == "learn":
        print("-" * 20)
        print()
        length =input("Short or long fact? ")
        if length.lower() == "short":
            print()
            print(random.choice(short_facts))
        if length.lower() == "long":
            print()
            print("Here's something interesting")
            print(random.choice(long_facts))
    
        stats["happiness"] += 5
        
    elif topic.lower() == "rest":
        print("Sounds good! Amiguito could use a little rest. Let's take a break and recharge!")
        stats["energy"] += 10
    elif topic.lower() == "drink":
        print("Refreshing! Amiguito loves to stay hydrated! Let's have some water together!")
        stats["thirst"] += 10
    elif topic.lower() == "exit":
        print("Goodbye! It was nice chatting with you!")
        break
    elif topic.lower() == "stats":
        amiguito.show_stats()
    elif topic.lower() == "mood":
        if not_so_good:
            print()
            print("I'm not feeling my best right now. Maybe we should do something to help me feel better!")
        if all_good:
            print()
            print("I am feeling great! Thanks for asking!")
        
    elif topic.lower() == "help":
        print()
        display_menu()
    elif topic.lower() == "hi":
        print("Hello! Amiguito is here to chat and have fun with you! What would you like to talk about?")
        stats["happiness"] += 5
    
    elif topic.lower() == "history":
        print("Event history:")
        for number, entry in enumerate (history):
            print(f"{number + 1}. {entry}")
    elif topic.lower() == "full":
        print("magic happened... Im all better now")
        for key in ["fullness", "thirst", "energy", "happiness"]:
            stats[key] += 100

    elif topic.lower() == "inventory":
        print("Here's my inventory: ")
        for item in amiguito.inventory:
            print()
            print("-", item)
            print()

    elif topic.lower() == "use":
        item = input("which item would you like to choose? ").lower()
        if item in items and item in amiguito.inventory:
            stat = items[item]["stat"]
            amount = items[item]["amount"]
            stats[stat] += amount
            amiguito.inventory.remove(item)
            print(items[item]["message"])
            print(f"{item} has been removed from your inventory.")
        else:
            print("I'm not sure if I have that. Let's try something else!")
            stats["happiness"] -= 5
    elif topic.lower() == "give":
        item = input("which item would you like to give me? ").lower()
        if item in items:
            amiguito.inventory.append(item)
            print(f"Thanks for giving me a {item}! I really appreciate it!")
        else:
            print("I'm not sure what that is. Let's try something else!")
            stats["happiness"] -= 5
   
    




    
    clamp_stats(stats)




    amiguito.state_of_being()

    with open("amiguito_state.json", "w") as file:
        json.dump ({"stats": stats, "inventory": amiguito.inventory}, file)





