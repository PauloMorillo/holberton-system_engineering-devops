# this file fix an error caused by too many files opened in nginx
exec { 'fix--for-nginx':
command  => 'sudo sed -i "1i worker_rlimit_nofile 30000;" "limits.conf" | sudo service nginx restart',
provider => shell,
cwd      => '/etc/security/',
path     => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
}