import { ComponentFixture, TestBed } from '@angular/core/testing';

import { HeatmapMissenseComponent } from './heatmap-missense.component';

describe('HeatmapMissenseComponent', () => {
  let component: HeatmapMissenseComponent;
  let fixture: ComponentFixture<HeatmapMissenseComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ HeatmapMissenseComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(HeatmapMissenseComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
