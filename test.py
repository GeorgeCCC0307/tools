import json
import subprocess
json_path = "/mnt/smbfs/George_Chang/test.json"
def exec_cmd( cmd):
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, encoding='utf-8')
    stdout,stderr = p.communicate()
    output=stdout.strip()
    ret=p.returncode
    return ret,output,stderr

def get_result( cmd):
    ret,out,err = exec_cmd(cmd)
    return out

def load_json():
    try:
        with open(json_path, 'r') as f:
            data = json.load(f)
        return data
    except FileNotFoundError:
        print("File not found.")
    except json.JSONDecodeError:
        print("JSON decoding failed.")

data={}
index = 0
def add_data():
    data['index'] = index
    index += 1
    data['content'] = []
    data['option'] = {}

def show_context(context_data):
    print("======================")
    for i in context_data['content']:
        print(i)

def get_option(data):
    question = ""
    cnt = 1
    for i in data["option"].keys():
        question += "{}. {} \n".format(cnt,i)
        cnt+=1
    val = input(question) 
    tmp =  list(data["option"].keys())
    return tmp[int(val)-1]

if __name__ == "__main__":
    a = load_json()
    # print(a['index'])
    # print(a['index']['0'])
    idx = '0'
    while True:
        show_context(a['index'][idx])
        opt = get_option(a['index'][idx])
        idx = a['index'][idx]["option"][opt]
        if idx == "Q":
            break;
        # print(opt)