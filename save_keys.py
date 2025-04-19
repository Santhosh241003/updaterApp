from pyupdater.core.key_handler.keys import Keys
import json
import os

def save_keys():
    # Generate keys
    kh = Keys()
    keypack = kh._gen_keypack('Santhosh')
    
    # Save to .pyupdater directory
    pyupdater_dir = os.path.join(os.getcwd(), '.pyupdater')
    keys_file = os.path.join(pyupdater_dir, 'keys.pyu')
    
    # Create keypack data
    key_data = {
        'app_private': keypack['repo']['app_private'],
        'app_public': keypack['upload']['app_public']
    }
    
    # Save keys
    with open(keys_file, 'w') as f:
        json.dump(key_data, f)
    
    print(f"Keys saved to {keys_file}")
    print(f"Public Key: {key_data['app_public']}")
    
if __name__ == '__main__':
    save_keys()
