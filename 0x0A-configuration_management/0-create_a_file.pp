$doc_root = "/tmp/holberton"

file { $doc_root:
 ensure => "file",
 owner => "www-data",
 group => "www-data",
 mode => 744,
 content => "I love Puppet"
}