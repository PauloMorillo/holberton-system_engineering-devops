# this file replaces a doble p from settings wordpress file
exec { 'fix-wordpress':
command  => 'sed -i "s/phpp/php/" wp-settings.php',
provider => shell,
cwd      => '/var/www/html/',
path     => '/usr/bin:/usr/sbin:/bin',
}
