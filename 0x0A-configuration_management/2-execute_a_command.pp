# this file kill a process by name
exec { 'killprocess':
command => '/usr/bin/pkill killmenow'
}
