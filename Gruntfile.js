module.exports = function(grunt) {
  grunt.initConfig({
    pkg: grunt.file.readJSON('package.json'),
    sass: {
      options: {
          loadPath: ['beckton/assets/vendor/foundation-sites/scss']
        },
      dist: {
        files: {
          'beckton/static/css/main.css' : 'beckton/assets/scss/main.scss'
        }
      }
    },
    cssmin: {
      target: {
        files: [{
          expand: true,
          cwd: 'beckton/static/css/',
          src: ['*.css', '!*.min.css'],
          dest: 'beckton/static/css/',
          ext: '.min.css'
        }]
      }
    },
    copy: {
      target: {
        files: [
          {
            expand: true,
            cwd: 'beckton/assets/javascript',
            src: ['*.js'],
            dest: 'beckton/static/javascript',
            filter: 'isFile'
          },
          {
            expand: true,
            cwd: 'beckton/assets/vendor/foundation-sites/dist',
            src: ['**/*.js'], 
            dest: 'beckton/static/vendor/foundation-sites', 
            filter: 'isFile'
          },
          {
            expand: true,
            cwd: 'beckton/assets/vendor/jquery/dist',
            src: ['**/*.js'], 
            dest: 'beckton/static/vendor/jquery', 
            filter: 'isFile'
          }
        ]
      }
    },
    watch: {
      css: {
        files: '**/*.scss',
        tasks: ['sass', 'cssmin']
      },
      scripts: {
        files: 'beckton/assets/**/*.js',
        tasks: ['copy']
      },
    }
  });
  grunt.loadNpmTasks('grunt-contrib-sass');
  grunt.loadNpmTasks('grunt-contrib-cssmin');
  grunt.loadNpmTasks('grunt-contrib-watch');
  grunt.loadNpmTasks('grunt-contrib-copy')
  grunt.registerTask('default',['watch']);
}
