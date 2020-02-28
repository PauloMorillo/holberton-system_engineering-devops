# this file fix an error caused by too many files opened in nginx
exec { 'fix--for-nginx':
command  => 'sudo sed -i "s/_processes 4;/_processes 7;/" "nginx.conf" | sudo service nginx restart',
provider => shell,
cwd      => '/etc/nginx/',
path     => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
}