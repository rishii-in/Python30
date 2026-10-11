print("="*50)
print("         🌐 URL SAFETY ANALYZER         ")                          
print("="*50)
print()
risk=0
count=0
url=input("Enter the URL:")
print()
url=url.strip()
url=url.lower()
if url.startswith("https://"):
    protocol="https ✅"
    status="Secure"
elif url.startswith("http://"):
    protocol = "http ❌"
    status="Not Secure"
    risk+=1
else:
    protocol="Unknown ❌"
    status="Invalid URL"
    risk+=2
domain=url.replace("https://","")
domain=url.replace("http://","")
Domain = domain.split("/")[0]
if "/" in domain:
    path = domain.split("/")[1]
else:
    path="/"
print("-"*50)
print("            🔍 URL ANALYSIS REPORT     ")
print("-"*50)
print()
print(f"URL       : {url}")
print(f"Protocol  : {protocol}")
print(f"Status    : {status}")
print(f"Domain    : {Domain}")
print(f"Path      : {path}")
print()
print("-"*50)
print()
if "login" in domain:
    print("⚠️  login detected")
    count+=1
    risk+=1
if "verify" in domain:
    print("⚠️  verify detected")
    count+=1
    risk+=1
if "update" in domain:
    print("⚠️  update detected")
    count+=1
    risk+=1
if "secure" in domain:
    print("⚠️  secure detected")
    count+=1
    risk+=1
if "account" in domain:
    print("⚠️  account detected")
    count+=1
    risk+=1
if "free" in domain:
    print("⚠️  free detected")
    count+=1
    risk+=1
if "signin" in domain:
    print("⚠️  bank detected")
    count+=1
    risk+=1
if count==0:
    print("Suspicious Keywords : None ✅")
else:
    print(f"Suspicious Keywords : {count} Detected 🚨 ")
if risk>=4:
    level="🔴 HIGH RISK"
elif risk>=2:
    level="🟡 SUSPICIOUS"
else:
    level="🟢 SAFE"
print(f"Risk Score : {risk}")
print(f"Risk Level : {level}")
print()
print("-"*50)
if level=="🔴 HIGH RISK":
    print("\n ⚠️  WARNING! ")
    print()
    print("Do Not :")
    print("❌ Click Suspicious Links")
    print("❌ Enter Your password")
    print("❌ Enter Your OTP")
    print("❌ Share Personal Information")
    print("❌ Make Payments")
    print() 
    print(" 🛡️  Recommended Actions:")
    print("✔️   Verify the link through an official channel.")
elif level=="🟡 SUSPICIOUS":
    print("\n ⚠️ BE CAREFUL!")
    print("\n🛡️  Recommended Action:")
    print(" Verify the website before entering information.")   
else:
    print("\n ✅ No obvious warning signs detected.")
    print("\n🛡️  Recommended Action:")
    print("Continue with normal online caution.") 
print()
print("="*50)
print("           🔐 ANALYSIS COMPLETED ")
print("="*50)
print()