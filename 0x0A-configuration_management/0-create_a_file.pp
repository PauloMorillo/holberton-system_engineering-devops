# this file create a file in tmp with puppet tool
$doc_root = '/tmp/holberton'

file { $doc_root:
ensure  => 'file',
owner   =>  'www-data',
group   => 'www-data',
mode    => '0744',
content => 'I love Puppet'
}
