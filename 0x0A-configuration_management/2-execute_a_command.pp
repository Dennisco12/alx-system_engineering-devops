# this kills the process named 'killmenow'

exec { 'killmenow':
command => 'pkill -f killmenow',
path    => '/usr/bin',
}
