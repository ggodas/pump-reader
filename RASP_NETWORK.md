
Instalar avari
sudo apt-get install avahi-utils

Editar
sudo vim  /etc/avahi/avahi-daemon.conf


[publish]
#disable-publishing=no
#disable-user-service-publishing=no
#add-service-cookie=no
publish-addresses=yes
publish-hinfo=yes
publish-workstation=yes
publish-domain=yes
#publish-dns-servers=192.168.50.1, 192.168.50.2
publish-resolv-conf-dns-servers=yes
#publish-aaaa-on-ipv4=yes
#publish-a-on-ipv6=no

Criar Arquivo /etc/avahi/services/multiple.service

<?xml version="1.0" standalone='no'?>
<!DOCTYPE service-group SYSTEM "avahi-service.dtd">
<service-group>
        <name replace-wildcards="yes">%h</name>
        <service>
                <type>_device-info._tcp</type>
                <port>0</port>
                <txt-record>model=RackMac</txt-record>
        </service>
        <service>
                <type>_ssh._tcp</type>
                <port>22</port>
        </service>
</service-group>


https://elinux.org/RPi_Advanced_Setup#Setting_up_for_remote_access_.2F_headless_operation