# define the CPT
p.intelligence <- c(0.7, 0.3)
p.difficulty <- c(0.6,0.4)
p.sat <- structure( c(0.95,0.2, 0.05,0.8), .Dim = as.integer(c(2,2)) )
p.grade <- structure( c(.3,.9,.05,.5, .4,.08,.25,.3, .3,.02,.7,.2), .Dim = as.integer(c(2,2,3)) )
p.letter <- structure( c(0.1,0.4,0.99, 0.9,0.6,0.01), .Dim = as.integer(c(3,2)))

# define the dirch prior for the CPT
alpha.letter <- structure( c(1,1,1, 1,1,1), .Dim = as.integer(c(3,2)) )
alpha.intelligence<- c(1,1)
alpha.difficulty <- c(1,1)
alpha.sat <- structure(c(1,1,1,1), .Dim=as.integer(c(2,2)))
alpha.grade<- structure( c(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1), .Dim = as.integer(c(2,2,3)) )

# define the probability to have NA in the data
p.lostData = 0.5

# define the number of instance
N <- 100

# generate the fake data based on known CPT
set.seed(124)
intelligence <- rep(0, times=N)
difficulty <- rep(0, times=N)
grade <- rep(0, times=N)
sat <- rep(0, times=N)
letter <- rep(0, times=N)
difficulty <- sample(c(1,2), N, replace=TRUE, prob=p.intelligence)
intelligence <- sample(c(1,2), N, replace=TRUE, prob=p.intelligence)
for (i in 1:N) {
  grade[i] <- sample(c(1,2,3), 1, replace=TRUE, prob=p.grade[intelligence[i], difficulty[i],])
  sat[i] <- sample(c(1,2), 1, replace=TRUE, prob=p.sat[intelligence[i],])
  
  letter[i] <- sample(c(1,2), 1, replace=TRUE, prob=p.letter[grade[i],])
}

# insert NA
for (i in 1:N) {
  num <- sample(c(0,1), 1, prob=c(p.lostData, 1 - p.lostData))
  if (num == 0) {
    intelligence[i] = NA
  }
  num <- sample(c(0,1), 1, prob=c(p.lostData, 1 - p.lostData))
  if (num == 0) {
    difficulty[i] = NA
  }
  num <- sample(c(0,1), 1, prob=c(p.lostData, 1 - p.lostData))
  if (num == 0) {
    letter[i] = NA
  }
  num <- sample(c(0,1), 1, prob=c(p.lostData, 1 - p.lostData))
  if (num == 0) {
    grade[i] = NA
  }
  num <- sample(c(0,1), 1, prob=c(p.lostData, 1 - p.lostData))
  if (num == 0) {
    sat[i] = NA
  }
}

# assumble the data
data_list = list ('alpha.letter' = alpha.letter,
                  'alpha.grade' = alpha.grade,
                  'alpha.sat' = alpha.sat,
                  'alpha.difficulty' = alpha.difficulty,
                  'alpha.intelligence' = alpha.intelligence,
                  'N' = N,
                  'intelligence' = intelligence,
                  'difficulty' = difficulty,
                  'sat' = sat,
                  'grade' = grade,
                  'letter' = letter)

# import the bug model
library('rjags')
library('coda')
jags <- jags.model('student3.bug',
                   data = data_list,
                   n.chains = 4,
                   n.adapt = 100)

# do the updating

update(jags, 10000)
# do the sampling
N_sample = 5000
# here we only monitor the c('p.letter', 'p.sat', 'p.difficulty', 'p.grade', 'p.intelligence')
sample_res<-coda.samples(jags,
                         c('p.letter', 'p.sat', 'p.difficulty', 'p.grade', 'p.intelligence'),
                         N_sample)
# plot the rest
plot(sample_res)