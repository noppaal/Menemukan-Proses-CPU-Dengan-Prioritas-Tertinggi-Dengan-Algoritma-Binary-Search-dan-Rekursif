import tkinter as tk
from tkinter import messagebox, simpledialog
import time
import sys
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import random

# Increase the recursion limit
sys.setrecursionlimit(3000)

# Daftar nama proses umum di Windows
process_names = [
    "System Idle Process", "System", "smss.exe", "csrss.exe", "wininit.exe", 
    "services.exe", "lsass.exe", "svchost.exe", "explorer.exe", "taskhostw.exe", 
    "spoolsv.exe", "dllhost.exe", "conhost.exe", "cmd.exe", "notepad.exe", 
    "chrome.exe", "firefox.exe", "edge.exe", "powershell.exe", "wmiprvse.exe", 
    "taskmgr.exe", "SearchIndexer.exe", "audiodg.exe", "sihost.exe", "RuntimeBroker.exe", 
    "msiexec.exe", "winlogon.exe", "win32k.sys", "mspmsnsv.exe", "eset_service.exe", 
    "wscntfy.exe", "backgroundTaskHost.exe", "dwm.exe", "msmpeng.exe", "cmd.exe", 
    "MicrosoftEdgeCP.exe", "MicrosoftEdge.exe", "taskeng.exe", "skype.exe", "OneDrive.exe", 
    "Dropbox.exe", "Spotify.exe", "vssvc.exe", "steam.exe", "teams.exe", 
    "Zoom.exe", "discord.exe", "java.exe", "javaw.exe", "javaws.exe", 
    "notepad++.exe", "vlc.exe", "skypehost.exe", "wmiadap.exe", "audiodg.exe", 
    "AarSvc.exe", "cortana.exe", "mspmsnsv.exe", "explorer.exe", "HWiNFO64.exe", 
    "shadowplay.exe", "nvcontainer.exe", "client.exe", "conhost.exe", "taskhost.exe", 
    "conhost.exe", "smss.exe", "rundll32.exe", "obssvc.exe", "servicingstack.exe", 
    "msfeedssync.exe", "chromium.exe", "skype.exe", "textinputhost.exe", "systemsettings.exe", 
    "searchfilterhost.exe", "searchprotocolhost.exe", "svchost.exe", "setup.exe", "wuauclt.exe", 
    "taskschd.dll", "ecmsvc.exe", "iexplore.exe", "chrome.exe", "firefox.exe", 
    "powershell_ise.exe", "msiexec.exe", "msdt.exe", "procexp.exe", "core.exe", 
    "lightshot.exe", "wscript.exe", "hl2.exe", "cmd.exe", "netstat.exe", 
    "ping.exe", "tftp.exe", "ftp.exe", "sfttray.exe", "firefox.exe", 
    "mspmsnsv.exe", "processhacker.exe", "optimus.exe", "fdm.exe", "sspd.exe", 
    "twauthapp.exe", "livecomm.exe", "spotify.exe", "conhost.exe", "totalcmd.exe", 
    "gadget.exe", "tunnelblick.exe", "exefile.exe", "qtcreator.exe", "gedit.exe", 
    "unity.exe", "xcopy.exe", "rpcnet.exe", "libreoffice.exe", "crashplan.exe", 
    "syncthing.exe", "httrack.exe", "scvhost.exe", "syncapp.exe", "blender.exe", 
    "javaw.exe", "opencpn.exe", "bluejeans.exe", "smss.exe", "findstr.exe", 
    "compress.exe", "pingtest.exe", "test.exe", "appdata.exe", "svchost.exe", 
    "dbus-daemon.exe", "sh.exe", "git.exe", "teamspeak.exe", "msagent.exe", 
    "shutdowm.exe", "install.exe", "android-debug.exe", "acrodist.exe", "console.exe", 
    "chromedriver.exe", "idownloader.exe", "iexplorer.exe", "taskmgr.exe", "uninstaller.exe", 
    "services.exe", "spoolsv.exe", "cmd.exe", "securom.exe", "ptfserver.exe", 
    "pandaclient.exe", "notepad.exe", "procmon.exe", "ipconfig.exe", "msvcr100.dll", 
    "blender.exe", "textedit.exe", "openvpn.exe", "opera.exe", "dd.exe", 
    "notepad++.exe", "contextmenu.exe", "element.exe", "mspmsnsv.exe", "mspmsnsv.exe", 
    "plugin-container.exe", "netstat.exe", "rpcss.exe", "smartscreen.exe", "python.exe", 
    "powershell.exe", "tcpsvcs.exe", "xfw.exe", "alft.exe", "tscon.exe", 
    "tskmgr.exe", "build.exe", "officeclicktorun.exe", "teams.exe", "winzip32.exe", 
    "daemon.exe", "allmspmsnsv.exe", "wmpnetwk.exe", "run.exe", "init.exe", 
    "message.exe", "valve.exe", "eqm.exe", "sdcnfg.exe", "rsync.exe", 
    "calibre.exe", "prl_tools.exe", "client64.exe", "start.exe", "diskpart.exe", 
    "mspmsnsv.exe", "robocopy.exe", "multimediadisp.exe", "itunes.exe", "yahoo.exe", 
    "ntvdm.exe", "hwbps.exe", "softwareupdate.exe", "windbg.exe", "svhost.exe", 
    "wininit.exe", "appwiz.exe", "usbmon.exe", "storage.exe", "cmd.exe", 
    "adobearm.exe", "ieframe.exe", "virtualbox.exe", "winver.exe", "applet.exe", 
    "hbr.exe", "cisvc.exe", "i386.exe", "extract.exe", "compmgmt.exe", 
    "macromed.exe", "at.exe", "osx.exe", "cfagent.exe", "mspmsnsv.exe", 
    "notepad.exe", "notepad++.exe", "ftpd.exe", "winbroadcaster.exe", "drive.exe", 
    "vmware-vmware.exe", "adobeupdater.exe", "vmtoolsd.exe", "printfilterpipelinehost.exe", "backgroundTaskHost.exe", 
    "taskhostw.exe", "tree.exe", "find.exe", "getmac.exe", "wpr.exe", 
    "explorer.exe", "mspmsnsv.exe", "powerchute.exe", "vxservice.exe", "nssm.exe", 
    "powercfg.exe", "nvsetup.exe", "tasklist.exe", "qbupdate.exe", "kmode.exe", 
    "nssm.exe", "tcpip.exe", "taskeng.exe", "screen.exe", "php.exe", 
    "pythonw.exe", "wuauserv.exe", "certreq.exe", "iexplore.exe", "tidy.exe", 
    "insight.exe", "blaze.exe", "windowexe.exe", "elasticsearch.exe", "cloudstation.exe", 
    "tuneup.exe", "optimus.exe", "inno.exe", "alps.exe", "explorer.exe", 
    "subprocess.exe", "perl.exe", "tlauncher.exe", "winapp.exe", "qemu.exe", 
    "dbgp.exe", "mspmsnsv.exe", "teams.exe", "npupdate.exe", "notepad.exe", 
    "command.exe", "explorer.exe", "synaptics.exe", "arc.exe", "arduino.exe", 
    "mspmsnsv.exe", "fileexplorer.exe", "overwolf.exe", "aim.exe", "bitdefender.exe", 
    "shadowplay.exe", "crossover.exe", "untrusted.exe", "gimp.exe", "program.exe", 
    "ace.exe", "ipv6.exe", "opera.exe", "socksv5.exe", "shutdown.exe", 
    "multiexec.exe", "inkscape.exe", "opera.exe", "enablermanager.exe", "rdesktop.exe", 
    "pdfpro.exe", "client.exe", "nxsvc.exe", "shell.exe", "bluestacks.exe", 
    "lss.exe", "svn.exe", "cryptsvc.exe", "freemake.exe", "geckodriver.exe", 
    "cisco.exe", "tmproxy.exe", "ideviceinstaller.exe", "modem.exe", "datamanager.exe", 
    "calibre.exe", "mobogenie.exe", "start.exe", "aero.exe", "ffmpeg.exe", 
    "portmapper.exe", "ccleaner.exe", "sol.exe", "hyperv.exe", "h2o.exe", 
    "verifier.exe", "python3.exe", "flow.exe", "vssvc.exe", "smartscreen.exe", 
    "win32k.exe", "safemode.exe", "mspmsnsv.exe", "proctools.exe", "apputil.exe", 
    "taskscheduler.exe", "safemode.exe", "tasklist.exe", "psql.exe", "rserver.exe", 
    "antivirus.exe", "searchfilterhost.exe", "iohandler.exe", "sessionmanager.exe", "prompt.exe", 
    "hwinfo.exe", "mus.exe", "dune.exe", "gserv.exe", "helper.exe", 
    "oracle.exe", "reinstall.exe", "defrag.exe", "procexp.exe", "wmp.exe", 
    "screenhost.exe", "securitycenter.exe", "mspmsnsv.exe", "driverquery.exe", "openssh.exe", 
    "instsrv.exe", "cmd.exe", "install.exe", "msiexec.exe", "system32.exe", 
    "aegis.exe", "curl.exe", "icon.exe", "cloudkey.exe", "tar.exe", 
    "restart.exe", "rr.exe", "zotero.exe", "appinstaller.exe", "vcruntime.exe", 
    "mspmsnsv.exe", "uvlauncher.exe", "pathfinder.exe", "tmexe.exe", "dbus.exe", 
    "explorer.exe", "tvsupport.exe", "mind.exe", "firefox.exe", "csc.exe", 
    "wordpad.exe", "regedit.exe", "wine.exe", "filezilla.exe", "beagle.exe", 
    "docker.exe", "ninja.exe", "json.exe", "virtualmachine.exe", "xnview.exe", 
    "treeview.exe", "multiplex.exe", "node.exe", "screenlocker.exe", "gimp.exe", 
    "cache.exe", "mspmsnsv.exe", "notepad.exe", "script.exe", "backup.exe", 
    "datadump.exe", "shield.exe", "xlaunch.exe", "storage.exe", "host.exe", 
    "lgservice.exe", "skypehost.exe", "fwsetup.exe", "cleanup.exe", "catalyst.exe", 
    "snappy.exe", "jetbrain.exe", "calc.exe", "machine.exe", "application.exe", 
    "mspmsnsv.exe", "servicehost.exe", "twin.exe", "taskhost.exe", "syswow64.exe", 
    "freeram.exe", "java.exe", "graph.exe", "mysqld.exe", "smartscreen.exe", 
    "explorer.exe", "installshell.exe", "service.exe", "cloud.exe", "iconifier.exe", 
    "torch.exe", "libreoffice.exe", "stunnel.exe", "stream.exe", "gnome.exe", 
    "deploy.exe", "setup.exe", "keygen.exe", "fixer.exe", "scrrun.exe", 
    "aide.exe", "elevate.exe", "batch.exe", "acronis.exe", "pythonw.exe", 
    "scanner.exe", "epicgameslauncher.exe", "gl.exe", "far.exe", "proex.exe", 
    "swole.exe", "nb.exe", "clienthost.exe", "pmf.exe", "shd.exe", 
    "pl.exe", "shellmgr.exe", "srvhost.exe", "du.exe", "directx.exe", 
    "gaia.exe", "trex.exe", "angry.exe", "zoo.exe", "compiler.exe", 
    "express.exe", "mini.exe", "pusher.exe", "miner.exe", "vrlauncher.exe", 
    "cmdm.exe", "safenet.exe", "hooker.exe", "game.exe", "lcore.exe", 
    "soundhost.exe", "doc.exe", "tconnect.exe", "system.exe", "cshell.exe", 
    "dmn.exe", "systask.exe", "cli.exe", "axshare.exe", "gamehost.exe"
]

# Membuat data proses dengan nama dan ID unik secara acak
processes = [f"{random.choice(process_names)}-{random.randint(1000, 99999)}" for _ in range(1000)]

# Sorting dengan insertion sort
def insertion_sort(processes):
    for i in range(1, len(processes)):
        key = processes[i]
        j = i - 1
        while j >= 0 and processes[j] > key:
            processes[j + 1] = processes[j]
            j -= 1
        processes[j + 1] = key

# Binary search dengan data yang sudah terurut dengan sorting
def iterative_binary_search(processes):
    insertion_sort(processes)
    low, high = 0, len(processes) - 1
    while low <= high:
        mid = (low + high) // 2
        if mid == len(processes) - 1:
            return processes[mid]
        low = mid + 1

# Rekursif dengan data yang belum disorting
def recursive_search(processes, index=0):
    if index == len(processes) - 1:
        return processes[index]
    current_process = processes[index]
    next_process = recursive_search(processes, index + 1)
    return current_process if current_process > next_process else next_process

# Function to find the highest priority process and measure execution time
def find_highest_priority():
    # Meminta input jumlah data
    options = [10, 20, 1000]
    num_processes = simpledialog.askinteger("Input", "Masukkan jumlah proses (10, 20, atau 1000):", initialvalue=10, minvalue=10, maxvalue=1000)
    if num_processes is None or num_processes not in options:
        messagebox.showerror("Error", "Jumlah proses harus 10, 20, atau 1000.")
        return

    # Membuat data proses dengan nama dan ID unik secara acak
    processes = [f"{random.choice(process_names)}-{random.randint(1000, 99999)}" for _ in range(num_processes)]

    # Measure execution time for iterative binary search (with sorting)
    start_time = time.perf_counter()
    highest_priority_process_iterative = iterative_binary_search(processes)
    iterative_time = time.perf_counter() - start_time

    # Measure execution time for recursive search (without sorting)
    start_time = time.perf_counter()
    highest_priority_process_recursive = recursive_search(processes)
    recursive_time = time.perf_counter() - start_time

    # Plot the execution times
    methods = ['Iterative Binary Search', 'Recursive Search']
    times = [iterative_time, recursive_time]

    fig, ax = plt.subplots()
    ax.bar(methods, times, color=['blue', 'green'])
    ax.set_xlabel('Search Method')
    ax.set_ylabel('Execution Time (seconds)')
    ax.set_title('Execution Time Comparison')

    # Embed the chart into Tkinter window
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()
    canvas.get_tk_widget().pack(pady=20)

    messagebox.showinfo("Result", f"Iterative Binary Search:\nProcess: {highest_priority_process_iterative}\nTime: {iterative_time:.6f} seconds\n\n"
                                  f"Recursive Search:\nProcess: {highest_priority_process_recursive}\nTime: {recursive_time:.6f} seconds")

# Create the main window
root = tk.Tk()
root.title("CPU Process Priority Finder")
root.geometry("600x400")
root.configure(bg='#f0f0f0')

# Create and style the title label
title_label = tk.Label(root, text="CPU Process Priority Finder", font=("Helvetica", 16, "bold"), bg='#f0f0f0')
title_label.pack(pady=10)

# Create and place the button
find_button = tk.Button(root, text="Find Highest Priority Process", command=find_highest_priority, bg='#0078D7', fg='white', font=("Helvetica", 12, "bold"), padx=10, pady=5)
find_button.pack(pady=20)

# Run the application
root.mainloop()
