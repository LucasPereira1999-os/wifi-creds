import subprocess
output1 = subprocess.check_output(["netsh", "wlan", "show", "profiles"],
                                  encoding="utf-8")

with open("../wifiscan.txt", "w") as f:
    f.write(output1)

password = []
with open("../wifiscan.txt", "r") as k:
    content = k.read()
    for i in content.splitlines():
        if "All User Profile" in i:
            value = i.split(":", 1)[1].strip()
            password.append(value)

print(password)

with open("../wifipwd.txt", "w") as c:
    for k in password:
        try:
            output = subprocess.check_output(["netsh", "wlan",
                                              "show", "profile",
                                              k, "key=clear"], encoding="utf-8")

            c.write(str(output))

        except subprocess.SubprocessError as e:
            c.write("something wrong")

