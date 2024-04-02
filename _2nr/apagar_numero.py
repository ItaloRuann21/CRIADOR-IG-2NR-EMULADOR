from time import sleep


def excluir_numero(device):
    try:
        # sair do 2nr
        device.app_stop('pl.rs.sip.softphone.newapp')
        sleep(2)
        
        # Abre o 2nr
        device.app_start('pl.rs.sip.softphone.newapp', use_monkey=True) 
        sleep(2)
        
        # Clica no numero
        device(resourceId='pl.rs.sip.softphone.newapp:id/phoneNumber').wait(30)
        device(resourceId='pl.rs.sip.softphone.newapp:id/phoneNumber').click()
        sleep(2)
        
        # Exclui numero
        device(text='Delete').wait(30)
        device(text='Delete').click()
        sleep(2)
        
        # Yes
        device(text='Yes').wait(30)
        device(text='Yes').click()
                
        return True
    except Exception as erro:
        print(erro)
        return False