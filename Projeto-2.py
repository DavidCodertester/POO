class VirtualMachine:
    def __init__(self, name, cpu, memory):
        self.name = name
        self.cpu = cpu
        self.memory = memory
        self.is_running = False

    def start(self):
        if not self.is_running:
            self.is_running = True
            print(f"{self.name} started.")

    def stop(self):
        if self.is_running:
            self.is_running = False
            print(f"{self.name} stopped.")

    def get_resource_usage(self):
        return self.cpu, self.memory


class ResourceManager:
    def __init__(self):
        self.virtual_machines = []

    def add_virtual_machine(self, vm):
        self.virtual_machines.append(vm)
        print(f"Added {vm.name} to the resource manager.")

    def show_resource_usage(self):
        total_cpu = 0
        total_memory = 0

        for vm in self.virtual_machines:
            if vm.is_running:
                cpu, memory = vm.get_resource_usage()
                total_cpu += cpu
                total_memory += memory

        print(f"Total CPU usage: {total_cpu} units")
        print(f"Total memory usage: {total_memory} MB")

    def start_all_virtual_machines(self):
        for vm in self.virtual_machines:
            if not vm.is_running:
                vm.start()

    def stop_all_virtual_machines(self):
        for vm in self.virtual_machines:
            if vm.is_running:
                vm.stop()

    def get_running_virtual_machines(self):
        running_vms = [vm for vm in self.virtual_machines if vm.is_running]
        return running_vms

    def get_virtual_machine_by_name(self, name):
        for vm in self.virtual_machines:
            if vm.name == name:
                return vm
        return None


# Criar instâncias de máquinas virtuais
vm1 = VirtualMachine("VM1", cpu=2, memory=4096)
vm2 = VirtualMachine("VM2", cpu=4, memory=8192)

# Criar gerenciador de recursos e adicionar máquinas virtuais
resource_manager = ResourceManager()
resource_manager.add_virtual_machine(vm1)
resource_manager.add_virtual_machine(vm2)

# Iniciar todas as máquinas virtuais
resource_manager.start_all_virtual_machines()

# Mostrar uso total de recursos
resource_manager.show_resource_usage()

# Parar todas as máquinas virtuais
resource_manager.stop_all_virtual_machines()

# Mostrar uso total de recursos novamente
resource_manager.show_resource_usage()

# Encontrar uma máquina virtual pelo nome
vm_name_to_find = "VM1"
found_vm = resource_manager.get_virtual_machine_by_name(vm_name_to_find)
if found_vm:
    print(f"Máquina virtual encontrada: {found_vm.name}")
else:
    print(f"Máquina virtual com o nome '{vm_name_to_find}' não encontrada.")
