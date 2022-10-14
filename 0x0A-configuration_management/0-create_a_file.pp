#This creates a file /tmpp/school
#File contains "I love puppet"

file { '/tmp/school':
mode    => '0744',
owner   => 'www-data',
group   => 'www-data',
content => 'I love Puppet',
}
