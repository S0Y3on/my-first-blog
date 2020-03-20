from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib import auth
from django.shortcuts import redirect
from address.models import Address

import os, pexpect
import pexpect.popen_spawn

new_account_command= 'geth --datadir "C:\ethereum\data" account new'
def createAccount(key):
    account = pexpect.popen_spawn.PopenSpawn(new_account_command,timeout=10)
    account.expect("Passphrase:")
    account.sendline(key)
    account.expect("Repeat passphrase:")
    account.sendline(key)
    # \nAddress: {a6933bbe6432c253cc33a139c78955c1658386d0}\n
    address = account.read().decode()[12:-2]
    # print(address,type(address))
    account.sendeof()
    return address

def signup(request):
    if request.method == "POST":
        if request.POST["password1"] == request.POST["password2"]:
            # password1==password2 , password1 으로 이더리움 계좌 생성 후 계좌 주소 address 저장
            addr = createAccount(request.POST["password1"])
            user = User.objects.create_user(
                username=request.POST["username"], password=request.POST["password1"]
            )
            address = Address()
            address.user = user
            address.addr = addr
            address.save()
            auth.login(request, user)
            return redirect('/')
        return render(request, 'signup.html')
    return render(request, 'signup.html')

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password = password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            return render(request, 'login.html', {'error': 'username or password is incorrect'})
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')
