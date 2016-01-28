var gulp = require('gulp');
var autoprefixer = require('gulp-autoprefixer');
var uglify = require('gulp-uglify');
var rename = require('gulp-rename');
var debug = require('gulp-debug');
var fs = require('fs');
var shell = require('gulp-shell');

var concat = require('gulp-concat');
var notify = require('gulp-notify');
var cache = require('gulp-cache');

var docsfiles = ['docs/*.rst'];

var readme = 'README.rst'
w = process.cwd();

var gulp = require('gulp')
var shell = require('gulp-shell')

gulp.task('build-docs', shell.task('bin/sphinx-build -W docs docs/html', {cwd: '.'}))

gulp.task('readme', shell.task('cp README.rst docs', {cwd: '.'}))

gulp.task('docs', ['build-docs'], function() {
  gulp.watch(readme, ['readme'])
  gulp.watch(['./docs/*.rst', './docs/*.py'], ['build-docs'])
})

/*

docs = gulp.task(
    'docs',
    function() {
        return gulp.src(docsfiles)
        .pipe(shell(['bin/sphinx-build -W docs docs/html']))
        .pipe(notify({message: 'Styles task complete'}))
    });

gulp.task('default', ['styles']);
gulp.task('watch', function() {
  gulp.watch(docsfiles, ['docs']);
});
*/
/* vim:set ft=javascript : */