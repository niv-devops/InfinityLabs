#Approved by: 

from pyVim.connect import SmartConnect, Disconnect
from pyVmomi import vim
import ssl

context = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
context.verify_mode = ssl.CERT_NONE 

server = '10.1.2.23'
usr_name = 'devops'
password = "Student2021!"
vm_name = 'Niv_VM'

def monitor_vm():
    """ Monitor VM's current state and start it if stopped """
    si = None
    try:
        si = SmartConnect(host=server, user=usr_name, pwd=password, sslContext=context)
        content = si.RetrieveContent()
        vm_view = content.viewManager.CreateContainerView(content.rootFolder, [vim.VirtualMachine], True)
        print(vm_view)
        vm = None
        for vm_obj in vm_view.view:
            if vm_obj.name == vm_name:
                vm = vm_obj
                break
        if vm:
            state = vm.runtime.powerState
            print(f"VM '{vm_name}' current state: {state}")

            if state == vim.VirtualMachinePowerState.poweredOff:
                print(f"Starting VM '{vm_name}'...")
                task = vm.PowerOnVM_Task()
                #while task.info.state == vim.TaskInfo.State.running:
                    #continue
                print(f"VM '{vm_name}' started successfully.")
            else:
                print(f"VM '{vm_name}' is already running.")
        else:
            print(f"VM '{vm_name}' not found.")

    except Exception as e:
        print(f"Error: {str(e)}")

    finally:
        if si:
            Disconnect(si)

if __name__ == "__main__":
    monitor_vm()