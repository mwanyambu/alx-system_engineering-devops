# a manifest that kills a process
exec { 'kill_killmenow':
  command     => 'pkill -f killmenow',
  refreshonly => true,
  onlyif      => 'pgrep -f killmenow',
}
