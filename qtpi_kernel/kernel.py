from ipykernel.kernelbase import Kernel

class QtpiKernel(Kernel):
    implementation = 'Qtpi'
    implementation_version = '1.0'
    language = 'qtpi'
    language_version = '0.1'
    language_info = {
        'name': 'Any text',
        'mimetype': 'text/plain',
        'file_extension': '.txt',
    }
    banner = "Qtpi kernel - Enables user to input qtpi syntax and run the quantum processes."

    def do_execute(self, code, silent, store_history=True, user_expressions=None,
                   allow_stdin=False):
        if not silent:
            with open("output.py","w") as f:
                f.write(code)
                f.close()
            with open("output.qtp","w") as a:
                a.write(code)
                a.close()
             
             # if code[0] == "%":
                  # cp = subprocess.Popen(["python3", "output.py"], stdout=subprocess.PIPE, stderr=subprocess.PIPE,)
             # else:
            
            cp = subprocess.Popen(["/home/miroslav/qtpi/Qtpi", "output.qtp"], stdout=subprocess.PIPE, stderr=subprocess.PIPE,)
            stdout_value, stderr_value = cp.communicate()
            stdOutput = repr(stdout_value)
            stdError = repr(stderr_value)
            fulloutput = str(cp.returncode)+ "\n***\n" + stdOutput + "\n***\n" + stdError + "\n***"
            # cp = subprocess.run(["/home/miroslav/qtpi/Qtpi", "output.qtp"], universal_newlines=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            # if cp.stdout != "":
            # output = cp.stdout
            # else:
            # output = cp.stderr
            stream_content = {'name': 'stdout', 'text': fulloutput}
            self.send_response(self.iopub_socket, 'stream', stream_content)
            
        return {'status': 'ok',
                # The base class increments the execution count
                'execution_count': self.execution_count,
                'payload': [],
                'user_expressions': {},
               }
