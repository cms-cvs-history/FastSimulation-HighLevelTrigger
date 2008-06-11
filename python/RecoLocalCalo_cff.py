import FWCore.ParameterSet.Config as cms

import FastSimulation.CaloRecHitsProducer.CaloRecHitCopy_cfi
hltEcalPreshowerRecHit = FastSimulation.CaloRecHitsProducer.CaloRecHitCopy_cfi.caloRecHitCopy.clone()
import FastSimulation.CaloRecHitsProducer.CaloRecHitCopy_cfi
hltEcalRecHit = FastSimulation.CaloRecHitsProducer.CaloRecHitCopy_cfi.caloRecHitCopy.clone()
import FastSimulation.CaloRecHitsProducer.CaloRecHitCopy_cfi
hltHbhereco = FastSimulation.CaloRecHitsProducer.CaloRecHitCopy_cfi.caloRecHitCopy.clone()
import FastSimulation.CaloRecHitsProducer.CaloRecHitCopy_cfi
hltHoreco = FastSimulation.CaloRecHitsProducer.CaloRecHitCopy_cfi.caloRecHitCopy.clone()
import FastSimulation.CaloRecHitsProducer.CaloRecHitCopy_cfi
hltHfreco = FastSimulation.CaloRecHitsProducer.CaloRecHitCopy_cfi.caloRecHitCopy.clone()
hltEcalPreshowerRecHit.OutputRecHitCollections = ['EcalRecHitsES']
hltEcalPreshowerRecHit.InputRecHitCollectionTypes = [1]
hltEcalPreshowerRecHit.InputRecHitCollections = cms.VInputTag(cms.InputTag("caloRecHits","EcalRecHitsES"))
hltHbhereco.OutputRecHitCollections = ['none']
hltHbhereco.InputRecHitCollectionTypes = [4]
hltHbhereco.InputRecHitCollections = ['caloRecHits']
hltHoreco.OutputRecHitCollections = ['none']
hltHoreco.InputRecHitCollectionTypes = [5]
hltHoreco.InputRecHitCollections = ['caloRecHits']
hltHfreco.OutputRecHitCollections = ['none']
hltHfreco.InputRecHitCollectionTypes = [6]
hltHfreco.InputRecHitCollections = ['caloRecHits']


