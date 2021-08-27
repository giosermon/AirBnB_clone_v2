# Configure a nginx server with header
exec {'execc_0':
  command => 'apt-get update -y',
  path    => '/usr/bin/'
}

group { 'execc_1':
  ensure => 'present'
}

user { 'execc_2':
  ensure  => 'present',
  groups  => 'ubuntu',
  require => Group['ubuntu']
}

file{'execc_3':
  ensure  => 'directory',
  owner   => 'ubuntu',
  group   => 'ubuntu',
  require => User['ubuntu']
}

file{'execc_4':
  ensure => 'directory',
  owner  => 'ubuntu',
  group  => 'ubuntu',
  require => User['ubuntu']
}

file{'execc_5':
  ensure => 'directory',
  owner  => 'ubuntu',
  group  => 'ubuntu',
  require => User['ubuntu']
}

file{'execc_6':
  ensure => 'directory',
  owner  => 'ubuntu',
  group  => 'ubuntu',
  require => User['ubuntu']
}

file{'execc_7':
  ensure => 'directory',
  owner  => 'ubuntu',
  group  => 'ubuntu',
  require => User['ubuntu']
}

file{'execc_8':
  ensure  => 'link',
  target  => '/data/web_static/releases/test',
  require => File['/data/web_static/releases/test']
}

exec{'execc_9':
  command => '/usr/bin/wget -q https://raw.githubusercontent.com/dario-castano/AirBnB_clone_v2/master/fake.html -O /data/web_static/releases/test/index.html',
  require => File['/data/web_static/releases/test']
}

package{'nginx':
  ensure   => 'installed',
  name     => 'nginx',
  provider => 'apt',
  require => Exec['apt_update']
}

exec{'download_conf':
  command => '/usr/bin/wget -q https://raw.githubusercontent.com/dario-castano/AirBnB_clone_v2/master/default.txt -O /etc/nginx/sites-available/default',
  require => Package['nginx']
}

service{'nginx_service':
  ensure  => 'running',
  name    => 'nginx',
  enable  => 'true',
  require => [Package['nginx'], Exec['download_conf']]
}

file{'/etc/nginx/sites-available/default':
  notify  => Service['nginx_service'],
  require => Package['nginx']
}
